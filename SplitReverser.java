public class SplitReverser implements IWordReverser {
	public String ReverseWords(String sentence) {
		return "Hi";
	}
	
	public static void main(String[] args) {
		(new SplitReverserTests()).Run();
	}
}

class SplitReverserTests extends ReverserTests {
	public SplitReverserTests() {
		mReverser = new RegexReverser();
	}
	
	public void Run() {
		PrintTestResult(TestReverseWords());	}
}
