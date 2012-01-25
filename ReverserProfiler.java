class ReverserProfiler {
	/** Current clock time, in milliseconds */
	private static long getTime() {
		return System.currentTimeMillis();
	}
	
	public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Usage: java ReverserProfiler <algorithm> <number of words> <number of iterations>");
		}
		IWordReverser reverser;
		if (args[0].equals("RegexReverser"))
			reverser = new RegexReverser();
		else if (args[0].equals("DoubleReverser"))
			reverser = new DoubleReverser();
		else {
			System.out.println("Unknown reverser implementation: " + args[0]);
			return;
		}	
		System.out.println("Reverser: " + args[0]);
			
		int numWords = 10;
		if (args.length > 1)
			numWords = Integer.valueOf(args[1]);
		String sentence = "";
		for (int i = 0; i < numWords; i++) {
			sentence = sentence + "Hello ";
		}	
		System.out.print(String.valueOf(numWords) + " words, reversed ");
		
		int numIterations = 100000;
		if (args.length > 2)
			numIterations = Integer.valueOf(args[2]);
		System.out.println(String.valueOf(numIterations) + " times");
		
		// Do numIterations reversals to get a time estimate
		long startingTime = getTime();
		for (int i = 0; i < numIterations; i++) {
			sentence = reverser.reverseWords(sentence);
		}
		long timeSpent = getTime()-startingTime;
		System.out.println("Clock time (seconds): " + String.valueOf(timeSpent/1000.0));
	}
}