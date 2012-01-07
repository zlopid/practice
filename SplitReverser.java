public class SplitReverser implements IWordReverser {
	public String reverseWords(String sentence) {
		String[] words = sentence.split("\\s");
		String[] whitespace = sentence.split("[^\\s]+");
		
		// Add the words to a buffer in reverse order
		StringBuffer reversedSentence = new StringBuffer();
		for (int i = words.length-1; i >= 0; --i) {
			reversedSentence.append(words[i]);
			if (i != 0)
				reversedSentence.append(whitespace[i]);
		}
		
		return reversedSentence.toString();
	}
	
	public static void main(String[] args) {
		(new SplitReverserTests()).run();
	}
}

class SplitReverserTests extends ReverserTests {
	public SplitReverserTests() {
		mReverser = new SplitReverser();
	}
}
