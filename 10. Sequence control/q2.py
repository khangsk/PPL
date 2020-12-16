    def visitId(self,ctx,o):
        left = o.isLeft
        for x in o.sym:
            if ctx.name == x.name:
                if type(x.value) is CName:
                    if left:
                        return self.emit.emitPUTSTATIC('MCClass' + '/' + x.name, x.mtype, o.frame), x.mtype
                    else:
                        return self.emit.emitGETSTATIC('MCClass' + '/' + x.name, x.mtype, o.frame), x.mtype
                else:
                    if left:
                        return self.emit.emitWRITEVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
                    else:
                        return self.emit.emitREADVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype