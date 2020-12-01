    def visitId(self,ctx,o):
        for x in o.sym:
            if ctx.name == x.name:
                if type(x.value) is CName:
                    return self.emit.emitGETSTATIC('MCClass' + '/' + x.name, x.mtype, o.frame), x.mtype
                else:
                    return self.emit.emitREADVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype