from visidata import Sheet, VisiData, ItemColumn, vd, AttrDict, Column, setitem

vd.memory = AttrDict()
vd.contexts += [vd.memory]

class MemorySheet(Sheet):
    rowtype = 'memos' # rowdef: keys into vd.memory
    columns = [
        Column('name', getter=lambda c,r: r, setter=lambda c,r,v: setitem(vd.memory, v, vd.memory[r])),
        Column('value', getter=lambda c,r: vd.memory[r], setter=lambda c,r,v: setitem(vd.memory, r, v)),
    ]

    @property
    def rows(self):
        return list(vd.memory.keys())

    @rows.setter
    def rows(self, v):
        pass


vd.memosSheet = MemorySheet('memos')


Sheet.addCommand('^[M', 'open-memos', 'vd.push(vd.memosSheet)')
Sheet.addCommand('^[m', 'memo-cell', 'vd.memory[input("assign "+cursorCol.getDisplayValue(cursorRow)+" to: ")] = cursorCol.getTypedValue(cursorRow)')