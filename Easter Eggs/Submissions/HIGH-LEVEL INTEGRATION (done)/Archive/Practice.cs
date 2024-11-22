using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Text;

namespace Program
{
    class Class
    {
        public int num;
    }

    class Practice
    {
        static void Main(string[] args)
        {
            Class myObj = new Class();

            myObj.num = 34;
            Console.WriteLine(myObj.num);
        }
    }
}