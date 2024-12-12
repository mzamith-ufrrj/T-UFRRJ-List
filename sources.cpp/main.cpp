/*
 * File Main
 * Traffic Cellular Automata simulation  TCA-S
 */


#include <cstdlib>
#include <string>


#include "Configure.hpp"
#include "CellularAutomata.hpp"
using namespace std;

int main(int ac, char **av)
{
   
   Configure        *configure        = new Configure();
   CellularAutomata *cellularAutomata = new CellularAutomata();
   
   configure->loadConfigFile(av[1]);
   configure->mDensity = stof(av[2]);

   cout << "\nStarting application" << endl;
   cout << endl;
   cout << "=====================================================" << endl;
   configure->print();

   exit(-1);
   cellularAutomata->init(configure);
   cellularAutomata->exec();

   delete cellularAutomata;
   delete configure;
   
   return EXIT_SUCCESS;
}

