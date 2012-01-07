public abstract class ReverserTests {
	protected int mTestNum;
	protected IWordReverser mReverser;
	
	/**
	 * Test the ReverseWords function and print the test result
	 * @return the number of failed tests
	 */
	protected int WordsOk(String input, String expected, String description) {
		mTestNum++;
		String actual = mReverser.ReverseWords(input);
		boolean passed = actual.equals(expected);
		System.out.print(passed? "ok " : "not ok ");
		System.out.print(String.valueOf(mTestNum) + " - " + description + " - ");
		System.out.println("ReverseWords(" + input + ") = " + actual + (!passed? "; expected: " + expected : ""));
		return passed? 0 : 1;
	}
	
	/**
	 * Run a suite of tests on the ReverseWords function of mReverser.
	 * @return the number of failed tests
	 */
	protected int TestReverseWords() {
		return WordsOk("Hi","Hi","Single word");
	}
	
	protected void PrintTestResult(int numFailedTests) {
		if (numFailedTests == 0) {
			System.out.println("# All tests passed!");
		} else {
			System.out.println("#" + String.valueOf(numFailedTests) + " tests failed");
		}
	}
	
	public abstract void Run();
}