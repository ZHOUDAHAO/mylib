#include<gtest/gtest.h>
#include<boost/format.hpp>
#include<iomanip>

auto int_plus_float(){
	int a=1;
	float b=2;
	return a+b;
}

auto digit_seperators(){
	auto a=1'000'000'000;
	auto b=-999'999'999;
	return a+b;
}
	

TEST(CPLUS14,AUTO){
	EXPECT_EQ(int_plus_float(),3.0);
}

TEST(CPLUS14,digit_seperators){
	EXPECT_EQ(digit_seperators(),1);
}

TEST(BOOST,NEW_FEATRUE){
	using namespace std;
	using boost::format;
	using boost::io::group;
	cout << format("%1% %2% %3% %2% %1% \n") % "o" % "oo" % "O";
	cout << format("_%|=6|_") % 1 << endl;
	vector<string>names(1, "Marc-Fran�ois Michel"), 
		surname(1,"Durand"), 
		tel(1, "+33 (0) 123 456 789");

	names.push_back("Jean"); 
	surname.push_back("de Lattre de Tassigny");
	tel.push_back("+33 (0) 987 654 321");

	for(unsigned int i=0; i<names.size(); ++i)
		cout << format("%1%, %2%, %|40t|%3%\n") % names[i] % surname[i] % tel[i];

	cerr << "\n\nEverything went OK, exiting. \n";
}

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
