class Cou_rep:
    def count_str(self):
        for i in range(0, len(in_str)):
            count = 0;
            for j in range(i + 1, len(in_str)):
                if (in_str[i] == in_str[j] and in_str[i] != ' '):
                    count = count + 1;
                    string = in_str[:j] + '0' + in_str[j + 1:];

            if (count > 1 and in_str[i] != '0'):
                print(in_str[i], " - ", count);

in_str = "welcome to the world of python programming"
c = Cou_rep()
c.count_str()