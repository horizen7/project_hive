#define WIN32_LEAN_AND_MEAN
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <string>
using namespace std;

int main(){

    //first initializing
    WSADATA wsa;
    int start = WSAStartup(MAKEWORD(2,2), &wsa);
    if (start != 0){
        cout << "WSAStartup failed: " << start << "\n";
        return 1;
    }
    //set socket
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sock == INVALID_SOCKET){
        cout << "Invalid Socket\n";
        return 1;
    }
    //creating IPv4 socket 

    //close and clean
    closesocket(sock);
    WSACleanup();

    return 0;
}


