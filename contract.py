# v2.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class TaskMarketplace(gl.Contract):
    tasks: TreeMap[Address, str]
    reputation_address: Address

    def __init__(self):
        # Hardcoded reputation address
        self.reputation_address = Address("0x77f86b0D8A0230BD612F41F9c638d682f6aBc476")

    @gl.public.write
    def create_task(self, description: str) -> None:
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
        user = gl.message.sender_address
        
        # Bigger reward for completing task
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(20))
        except:
            pass

    @gl.public.view
    def my_task(self) -> str:
        user = gl.message.sender_address
        return self.tasks.get(user, "")
