#define WIN32_LEAN_AND_MEAN
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <string>
using namespace std;

int main(){

    //first initializing
    WSADATA wsa;
    int node = WSAStartup(MAKEWORD(2,2), &wsa);

    //set socket
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    
    //close socket
    closesocket(sock);
    //cleanup
    WSACleanup();
}


