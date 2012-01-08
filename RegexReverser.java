import java.util.regex.*;
import java.util.LinkedList;

public class RegexReverser implements IWordReverser {
	public String reverseWords(String sentence) {
		Pattern wordOrWhitespace = Pattern.compile("[^\\s]+|\\s+");
		Matcher words = wordOrWhitespace.matcher(sentence);
		
		// Store all the matches in reverse order
		LinkedList<String> splitWords = new LinkedList<String>();
		while(words.find())
			splitWords.push(words.group());		 
		// Add each of the matches to the string buffer
		StringBuffer reversedSentence = new StringBuffer();
		while(splitWords.size() > 0)
			reversedSentence.append(splitWords.pop());

		return reversedSentence.toString();
	}
	
	public static void main(String[] args) {
		(new RegexReverserTests()).run();
	}
}

class RegexReverserTests extends ReverserTests {
	public RegexReverserTests() {
		mReverser = new RegexReverser();
	}
}
