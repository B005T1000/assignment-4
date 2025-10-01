"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise. """



def has_duplicates(product_ids):
    # Using a set is ideal here because it automatically stores only unique elements.
    # Each lookup and insertion into a set is O(1) on average, so as we iterate 
    # through the list we can quickly detect if an element has already been seen.
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.queue = []  # use a normal list

    def add_task(self, task):
        # append at the end → O(1)
        self.queue.append(task)

    def remove_oldest_task(self):
        # remove from the front → O(n), because all elements get shifted
        if self.queue:
            return self.queue.pop(0)
        return None



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        # A set is chosen because it stores only unique elements and provides O(1) 
        # average time complexity for both insertions and lookups.
        self.values = set()

    def add(self, value):
        # Adding a value to the set is O(1) on average.
        self.values.add(value)

    def get_unique_count(self):
        # Getting the size of a set is O(1).
        return len(self.values)
