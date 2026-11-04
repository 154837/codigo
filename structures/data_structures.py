
class Stack:
    """Manage affiliates using the LIFO principle."""

    def __init__(self):
        self.items = []

    def push(self, affiliate):
        """Add an affiliate to the top of the stack."""
        self.items.append(affiliate)

    def pop(self):
        """Remove and return the last affiliate."""
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        """Return the last affiliate without removing it."""
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0

    def get_all(self):
        """Return all affiliates from top to bottom."""
        return list(reversed(self.items))

    def size(self):
        """Return the number of affiliates."""
        return len(self.items)


class Queue:
    """Manage affiliates using the FIFO principle."""

    def __init__(self):
        self.items = []

    def enqueue(self, affiliate):
        """Add an affiliate to the end of the queue."""
        self.items.append(affiliate)

    def dequeue(self):
        """Remove and return the first affiliate."""
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        """Return the first affiliate without removing it."""
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self.items) == 0

    def get_all(self):
        """Return all affiliates from first to last."""
        return self.items.copy()

    def size(self):
        """Return the number of affiliates."""
        return len(self.items)


class AffiliateList:
    """Manage affiliates using a regular list."""

    def __init__(self):
        self.items = []

    def add(self, affiliate):
        """Add an affiliate to the list."""
        self.items.append(affiliate)

    def remove(self, identification):
        """Remove an affiliate using its identification."""
        for index, affiliate in enumerate(self.items):
            if affiliate.identification == identification:
                return self.items.pop(index)

        return None

    def search(self, identification):
        """Search for an affiliate by identification."""
        for affiliate in self.items:
            if affiliate.identification == identification:
                return affiliate

        return None

    def get_all(self):
        """Return all affiliates."""
        return self.items.copy()

    def is_empty(self):
        """Check whether the list is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of affiliates."""
        return len(self.items)
