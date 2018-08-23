package trygopy

type GoMessage struct {
	Number  int
	String  string
	Decimal float64
}

func EchoGoMessage(s GoMessage) GoMessage {
	return s
}

/* This is not yet supported
func BatchEchoGoMessage(s []GoMessage) []GoMessage {
	return s
}
*/
