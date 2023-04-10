


class History(object):
    def __init__(self):
        self._stack_undo = []
        self._stack_redo = []
    
    def __str__(self):
        str_undo_stack = '[]'
        str_redo_stack = '[]'
        if self._stack_undo:
            str_undo_stack = ''.join(['[%s]'%(st) for st in self._stack_undo])        
        if self._stack_redo:
            str_redo_stack = ''.join(['[%s]'%(st) for st in self._stack_redo])        
        return "CURRENT: %s\nUNDO: %s\nREDO: %s"%(self.current_state,
                                                  str_undo_stack,
                                                  str_redo_stack)

    @property
    def current_state(self):
        if not self.is_empty():
            return self._stack_undo[-1]
        else:
            print("None")
            exit()
    
    def append(self, state):
        self._stack_undo.append(state)
        self._stack_redo.clear()
    
    def undo(self):
        if not self.is_empty():
            state = self._stack_undo.pop()
            self._stack_redo.append(state)
    
    def redo(self):
        if not self._stack_redo:
            return
        state = self._stack_redo.pop()
        self._stack_undo.append(state)       
    
    def clear(self):
        self._stack_undo.clear()
        self._stack_redo.clear()
