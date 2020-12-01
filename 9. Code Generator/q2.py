    def visitFLoatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(str(ctx.value), o.frame), FloatType()