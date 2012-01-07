public class SplitReverser implements IWordReverser {
	public String ReverseWords(String sentence) {
		String[] words = sentence.split("\\s");
		
		// Add the words to a buffer in reverse order
		StringBuffer reversedSentence = new StringBuffer();
		for (int i = words.length-1; i >= 0; --i) {
			reversedSentence.append(words[i]);
			if (i != 0)
				reversedSentence.append(" ");
		}
		
		return reversedSentence.toString();
	}
	
	public static void main(String[] args) {
		(new SplitReverserTests()).Run();
	}
}

class SplitReverserTests extends ReverserTests {
	public SplitReverserTests() {
		mReverser = new SplitReverser();
	}
	
	public void Run() {
		PrintTestResult(TestReverseWords());	}
}
