package server;

public class ErrorMessage {
	private final ErrorType err;
	private final String message;

	public ErrorMessage(ErrorType err, String message) {
		this.err = err;
		this.message = message;
	}

	public String getErrorMessage() {
		return err.name() + ':' + err.getErrorDescription() + message;
	}
}
