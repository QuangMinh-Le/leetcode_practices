class MyCalendar:
    def __init__(self):
        self.bookings = []  # This will store the intervals
    
    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing bookings
        for booking in self.bookings:
            if not (end <= booking[0] or start >= booking[1]):  # If there's an overlap
                return False
        
        # No overlap, so we can book the new event
        self.bookings.append([start, end])
        # Sort bookings to keep them ordered (optional but useful)
        self.bookings.sort()  
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)