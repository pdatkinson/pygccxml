#ifndef simple_h
#define simple_h

#include <iostream>
class base
{
public:
  base() {};
  ~base() {};
  virtual int goodbye(int num_ref, int num_times) = 0;
};

class simple : public base
{
public:
  simple() {};
  ~simple() {};
  int hello() { return 0; };
  int goodbye(int , int) override
    {
      std::cout << "goodbye\n";
      return 10;
    } ;
};

#endif
