from mem0 import MemoryClient
import os

memory = MemoryClient(
    api_key=os.getenv("MEM0_API_KEY")
)