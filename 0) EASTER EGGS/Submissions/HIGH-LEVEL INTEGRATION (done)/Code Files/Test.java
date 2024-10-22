import java.util.Map;
import java.util.HashMap;

class Test
{
	public static void main(String[] args)
	{
		Map <String,String> map = new HashMap<>();

		map.put("switch","on");
		map.put("fan","off");

		System.out.println(map);
	}
}