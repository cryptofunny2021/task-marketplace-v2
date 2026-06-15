# v2.5 Stable
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class TaskMarketplace(gl.Contract):
    tasks: TreeMap[Address, str]
    scores: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def create_task(self, description: str) -> None:
        user = gl.message.sender_address
        self.tasks[user] = description
        current = self.scores.get(user, u256(0))
        self.scores[user] = current + u256(5)

    @gl.public.write
    def complete_task(self) -> None:
        user = gl.message.sender_address
        current = self.scores.get(user, u256(0))
        self.scores[user] = current + u256(20)

    @gl.public.view
    def my_task(self) -> str:
        user = gl.message.sender_address
        return self.tasks.get(user, "")

    @gl.public.view
    def my_score(self) -> u256:
        user = gl.message.sender_address
        return self.scores.get(user, u256(0))
