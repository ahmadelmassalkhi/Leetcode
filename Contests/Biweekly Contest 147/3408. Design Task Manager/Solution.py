import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # priority queue
        self.heap = [Task(userId, taskId, priority) for userId, taskId, priority in tasks]
        heapq.heapify(self.heap)
        
        # cache for quick lookup
        self.map = {taskId: [priority, userId] for userId, taskId, priority in tasks}
        
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        # task guaranteed NOT to exist in the system
        heapq.heappush(self.heap, Task(userId, taskId, priority))
        self.map[taskId] = [priority, userId]
        

    def edit(self, taskId: int, newPriority: int) -> None:
        # task guaranteed to exist in the system
        self.add(self.map[taskId][1], taskId, newPriority)

        
    def rmv(self, taskId: int) -> None:
        del self.map[taskId]

        
    def execTop(self) -> int:
        while self.heap:
            task = heapq.heappop(self.heap)
            # check if task is valid (not deleted) & up to date (latest edit)
            if task.taskId in self.map and self.map[task.taskId]==[task.priority, task.userId]:
                del self.map[task.taskId]
                return task.userId
        return -1

    
class Task:
    def __init__(self, userId, taskId, priority):
        self.userId = userId
        self.taskId = taskId
        self.priority = priority
    
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.taskId > other.taskId
        return self.priority > other.priority


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()