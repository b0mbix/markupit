import re
from typing import Any


class BlockState:
    """ 
    State used to save blocks and current cursor position in file. 
    """

    ENDLINE = re.compile(r"\n|$")

    def __init__(self, parent: Any = None) -> None:
        self.parse_text = ""
        self.blocks = []

        self.cursor_pos = 0
        self.max_cursor_pos = 0

        self.parent = parent

    @property
    def last_block(self) -> Any:
        if self.blocks:
            return self.blocks[-1]
        
    @property
    def nesting_lvl(self) -> int:
        lvl = 0
        state = self.parent
        while state:
            state = state.parent
            lvl += 1
        return lvl
    
    def init_parse_text(self, source: str) -> None:
        self.parse_text = source
        self.max_cursor_pos = len(source)
    
    def init_child_state(self, source: str) -> "BlockState":
        state = self.__class__(self)
        state.init_parse_text(source)
        return state
    
    def get_text_before(self, end_pos: int) -> str:
        return self.parse_text[self.cursor_pos:end_pos]
    
    def append(self, block: dict[str, Any]) -> None:
        self.blocks.append(block)
    
    def insert_second_to_last(self, block: dict[str, Any]) -> None:
        self.blocks.insert(len(self.blocks) - 1, block)

    def find_endline(self) -> int:
        match = self.ENDLINE.search(self.parse_text, self.cursor_pos)
        return match.end() if match else self.max_cursor_pos
    
    def add_para(self, text: str) -> None:
        # Para is the most general block type, that can match regex for other blocks.
        # Therefore, it is added to the list of blocks only if no other block is matched.
        # And it's handy to have such function directly in the state.

        if self.last_block and self.last_block["type"] == "Para":
            self.last_block["content"] += text
        else:
            self.append({"type": "Para", "content": text})
    
    def append_para(self) -> int | None:
        if not self.last_block or self.last_block["type"] != "Para":
            return None
        
        para_end = self.find_endline()
        self.last_block["content"] += self.get_text_before(para_end)
        return para_end
