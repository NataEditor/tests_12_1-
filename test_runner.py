import runner
import unittest

class RunnerTest(unittest.TestCase):


    def test_walk(self):
        obj_runner = runner.Runner(name='Тимохей')
        for _ in range(10):
            obj_runner.walk()
        self.assertEqual(obj_runner.distance, 50)


    def test_run(self):
        obj_runner = runner.Runner(name='Тимохей')
        for _ in range(10):
            obj_runner.run()
        self.assertEqual(obj_runner.distance, 100)

    def test_challenge(self):
        obj_w = runner.Runner(name='Тим')
        obj_r =runner.Runner(name='Митя')
        for _ in range(10):
            obj_r.run()
            obj_w.walk()
        self.assertNotEqual(obj_r.distance, obj_w.distance)


if __name__ == '__main__':
    unittest.main()