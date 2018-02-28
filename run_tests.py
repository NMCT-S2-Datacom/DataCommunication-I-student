import json
from unittest import TextTestRunner, TestLoader, TextTestResult, TestSuite

import os

PASS = 'PASS'
FAIL = 'FAIL'
ERROR = 'ERROR'
SKIP = 'SKIP'

TOTAL = 'Total'
COUNTER = {PASS: 0, FAIL: 0, SKIP: 0, ERROR: 0, TOTAL: 0}


class CustomTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.successes = []
        self.results = {TOTAL: COUNTER.copy()}

    def addSuccess(self, test):
        if '_example' in test._testMethodName:
            self.testsRun -= 1
            return
        super().addSuccess(test)
        self.successes.append(test)
        self.save_result(test, PASS)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.save_result(test, FAIL, err[1].args[0])

    def addError(self, test, err):
        super().addError(test, err)
        self.save_result(test, ERROR, err[1].args[0])

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.save_result(test, SKIP, reason)

    def save_result(self, test, code, msg=''):
        cat, week = test.__module__.split('.')
        week = week[:6]
        cls = test.__class__.__name__
        self.results[TOTAL][code] += 1
        self.results[TOTAL][TOTAL] += 1
        self.results.setdefault(cat, {TOTAL: COUNTER.copy()})
        self.results[cat][TOTAL][code] += 1
        self.results[cat][TOTAL][TOTAL] += 1
        self.results[cat].setdefault(week, {TOTAL: COUNTER.copy()})
        self.results[cat][week][TOTAL][code] += 1
        self.results[cat][week][TOTAL][TOTAL] += 1
        self.results[cat][week].setdefault(cls, {TOTAL: COUNTER.copy()})
        self.results[cat][week][cls][TOTAL][code] += 1
        self.results[cat][week][cls][TOTAL][TOTAL] += 1
        self.results[cat][week][cls][test._testMethodName] = code, msg

    def __getitem__(self, item):
        return self.results.__getitem__(item)


if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite()

    suite.addTests(loader.discover('.', 'week*.py'))

    with open(os.devnull, 'w') as null_stream:
        runner = TextTestRunner(stream=null_stream, resultclass=CustomTestResult, verbosity=1)
        result = runner.run(suite)

    print('\n\n###RESULTDATA###\n{res}\n###ENDRESULT###\n'
          .format(res=json.dumps(result.results)))

    ratio = len(result.successes) / result.testsRun

    print("\nFailed tests:")
    for fail in result.failures:
        print(' {}.{}.{}'.format(fail[0].__module__, fail[0].__class__.__name__, fail[0]._testMethodName))

    print("\nTest summary:")
    for cat in 'test', 'oefeningen':
        print('-' * 70)
        print('| {n:<10} |  PASS  |  FAIL  |  SKIP  |  ERROR  |  Total  |    %   |'.format(n=cat))
        print('-' * 70)
        for week in [week for week in result[cat] if week is not TOTAL]:
            print('| {n:<10} | {PASS:^6} | {FAIL:^6} | {SKIP:^6} | {ERROR:^7} | {Total:^7} | {r:^6.1%} |'
                  .format(n=week,
                          r=result[cat][week][TOTAL][PASS] / result[cat][week][TOTAL][TOTAL],
                          **result[cat][week][TOTAL]))
        print('| {n:<10} | {PASS:^6} | {FAIL:^6} | {SKIP:^6} | {ERROR:^7} | {Total:^7} | {r:^6.1%} |'
              .format(n=TOTAL,
                      r=result[cat][TOTAL][PASS] / result[cat][TOTAL][TOTAL],
                      **result[cat][TOTAL]))
    print('=' * 70)
    print('| {n:<10} | {PASS:^6} | {FAIL:^6} | {SKIP:^6} | {ERROR:^7} | {Total:^7} | {r:^6.1%} |'
          .format(n=TOTAL,
                  r=result[TOTAL][PASS] / result[TOTAL][TOTAL],
                  **result[TOTAL]))
    print('-' * 70 + '\n')

    if result.wasSuccessful():
        exit(0)
    exit(1)
