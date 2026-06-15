# Task Marketplace v2.0
# Task System with Automatic Rewards

from genlayer import *

class TaskMarketplace(gl.Contract):
    tasks: TreeMap[Address, str]
    reputation_address: Address

    def __init__(self, rep_addr: Address):
        self.reputation_address = rep_addr

    @gl.public.write
    def create_task(self, description: str) -> None:
        """Create a new task"""
        user = gl.message.sender_address
        self.tasks[user] = description
        
        # Reward for creating task
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(5))
        except:
            pass

    @gl.public.write
    def complete_task(self) -> None:
        """Complete a task and earn bigger reward"""
        user = gl.message.sender_address
        
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(20))  # Higher reward for completion
        except:
            pass

    @gl.public.view
    def my_task(self) -> str:
        """Get my current task"""
        return self.tasks.get(gl.message.sender_address, "")
