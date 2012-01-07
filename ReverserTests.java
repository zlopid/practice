public abstract class ReverserTests {
	protected int mTestNum;
	protected IWordReverser mReverser;
	
	/**
	 * Test the reverseWords function and print the test result
	 * @return the number of failed tests
	 */
	protected int ok(String input, String expected, String description) {
		mTestNum++;
		String actual = mReverser.reverseWords(input);
		boolean passed = actual.equals(expected);
		System.out.print(passed? "ok " : "not ok ");
		System.out.print(String.valueOf(mTestNum) + " - " + description + " - ");
		System.out.println(input + " => " + actual + (!passed? "; expected: " + expected : ""));
		return passed? 0 : 1;
	}
	
	/**
	 * Run a suite of tests on the reverseWords function of mReverser.
	 * @return the number of failed tests
	 */
	protected int testReverseWords() {
		return ok("Hi","Hi","Single word")
			+ ok("Hello world", "world Hello", "Two words")
			+ ok("I am a cat.","cat. a am I", "Short odd-words sentence")
			+ ok("Hello Dear,\tGoodbye","Goodbye\tDear, Hello", "Non-space whitespace");
	}
	
	protected void printTestResult(int numFailedTests) {
		if (numFailedTests == 0) {
			System.out.println("# All tests passed!");
		} else {
			System.out.println("#" + String.valueOf(numFailedTests) + " tests failed");
		}
	}

	public void run() {
		printTestResult(testReverseWords());
	}
}