class Solution {
    public int romanToInt(String s) {
        String[] romanChars = { "I", "V", "X", "L", "C", "D", "M"};
        int[] romanValues = { 1, 5, 10, 50, 100, 500, 1000};
                int pos = 0;
                int totalValue = 0;
                int currentValue = 0;
                int lastValue = 0;

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < romanChars.length; j++) {
                if (romanChars[j].equals(String.valueOf(s.charAt(i)))) {
                    currentValue = romanValues[j];
                    pos = j;
                }
            }

            if (pos > 0 && currentValue > lastValue) {
                totalValue += currentValue - lastValue * 2;
            } else {
                totalValue += currentValue;
            }

            lastValue = currentValue;
        }

        return totalValue;
    }
}