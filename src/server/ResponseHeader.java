package server;

public enum ResponseHeader {
	ERROR("responsetype=ERROR"),
	SENDMESSAGE("responsetype=MESSAGE"),
	INCOMINGCALL("responsetype=INCOMING_CALL"),
	CALLACCEPTED("responsetype=STATUS_REPORT"),
	CALLDECLINED("responsetype=CALL_DECLINED"), 
	CALLTIMEOUT("responsetype=CALL_TIMEOUT"), 
	CALLTERMINATE("responsetype=CALL_TERMINATE"),
	CALLABORT("responsetype=CALL_ABORT"), 
	OK("responsetype=OK");
	
	private final String header;
	
	ResponseHeader(String header) {
		this.header = header;
	}
	
	public String getHeader() {
		return header;
	}
	
}
