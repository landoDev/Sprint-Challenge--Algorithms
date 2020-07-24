class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Plan
        # Use selection sort to sort the list
        # have to go through the whole list 
            # for each part of the list 
            # see if the value at the index is the smallest in all the numbers after
        # for the length of the list - 1
        # maybe while robot can move right
            # initialize the current index
            # initialize the smallest index
            # starting at the current index and for every element until the end of the list
                # if the item is smaller than the smallest index
                    # smallest index = item
                    # pick up that item, take it to the smallest index then return to that spot in the loop and give it the previous smallest index
        # iterate through the given list
        # we may not have to account for - 1
        # for item in range(0, len(l)):
            # initialize the current position
            # pick up the first item
            # index = item # self._position
            # self.item = l[index] # l[self._position]
            # smallest_index = index
            # # while there is list left
            # for unsorted in range(index, len(l))
            #     # move
            #     self.move_right()
            #     check = self.compare_item() 
            #     # check returns 1 if held item is greater, 0 if it is equal and -1 if it's less than
            #     # check if smaller than held item
            #     if check >= 0:
            #         # check if that item is smaller than smallest index
            #         if smallest_index > self.item
        # bubble sort plan given the methods we were given
        # set master length
        self.set_light_on()
        end = len(self._list)
        # loop through the list
        for item in range(end - 1):
            # while robot can move right
            # grab the item at the current index
            
            while self.can_move_right():
                self._item = self._list[self._position]
                self.move_right()
                # compare the next item with the current item
                check = self.compare_item()
                # if the held item is greater than the item in front of it
                if check > 0:
                    # swap items
                    self.swap_item()
                    # move left and swap to finish swap
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            # move back to start
            while self.can_move_left():
                self.move_left()
        self.set_light_off()
                    

                    





if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)