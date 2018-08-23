import bind.trygopy

msg1 = bind.trygopy.GoMessage(1, "test", 1.1)
print(bind.trygopy.EchoGoMessage(msg1))

msg2 = bind.trygopy.GoMessage(Int=1, String="test", Decimal=3.14)
print(bind.trygopy.EchoGoMessage(msg2))

msgs = [msg1, msg2]
print(bind.trygopy.BatchEchoGoMessage(msgs))