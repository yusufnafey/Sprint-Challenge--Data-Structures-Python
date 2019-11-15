class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if capacity is >= to current, reset the current back to 0
    if self.current >= self.capacity:
      self.current = 0
    # store item and add to counter
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    # if its not none, get item
    return [item for item in self.storage if item != None]