public class Solution {

    public static int solution(int number) {
        int res = 0;
        for (int i = 0; i < number; i++) {
            res += (i % 3 == 0 || i % 5 == 0) ? i : 0;
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(solution(10));
    }
}
