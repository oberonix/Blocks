#include "BlocksGame.h"
using namespace std;

int main(int argc, char *argv[])
{
    BlocksGame::inst()->run(argc, argv);
    return EXIT_SUCCESS;
}
