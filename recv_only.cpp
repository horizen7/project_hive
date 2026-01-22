#define WIN32_LEAN_AND_MEAN
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <string>
using namespace std;
#pragma comment (lib, "Ws2_32.lib")

int main(){

    //first initializing Winsock (required on windows)
    WSADATA wsa{};
    int node = WSAStartup(MAKEWORD(2,2), &wsa);
    if (node != 0) {
        std::cerr << "WSAStartup failed! \n";
        return 1;
    }


    //create the UDP socket 
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP); //specifying UDP sockets; AF_INET is some constant IP protocol regarding internet access
    if (sock == INVALID_SOCKET){
        std::cerr << "Socket failed due to: " << WSAGetLastError() << "\n";
        WSACleanup();
        return 1;
    }

    //bind to a local port so the OS can send messages to us -- why necessarily the OS in this context?
    sockaddr_in local{}; //define socket type that is more versatile than sockaddr --  this is why it used and just recasted in the parameters of bind!
    local.sin_family = AF_INET; // specifies ip type to IPv4
    local.sin_port = htons(5000); //htons (host to network short) ensures data is interpreted correctly accross networks since there are many ways to store multi-byte numbers
    local.sin_addr.s_addr = htonl(INADDR_ANY); //htonl (host to network long) INADDR_ANY is the port 0.0.0.0, is stored in the attributed struct

    if (bind(sock, (sockaddr*)&local, sizeof(local)) == SOCKET_ERROR){ //bind takes arguments of the socket, a pointer that points to loacl but casts it as a different object type (why?), and the byte size of local
        std::cerr << "binding failed: " << WSAGetLastError() << "\n";   // << is outputting operator potentially
        closesocket(sock);
        WSACleanup();
        return 1;
    } 

    std::cout << "Listening on port 5000..."; 

    //receive datagrams forever (why forever? Do they normally delete after short notice? - maybe evident through the while true loop
    char buf[2048];
    while (true) {
        sockaddr_in from{}; //receiving socket
        int fromLen = sizeof(from);
        int n = recvfrom(sock, buf, (int)sizeof(buf) - 1, 0, (sockaddr*)&from, &fromLen); // reads data from a socket; maybe (int)sizeof... is a type of casting


    }


    //close socket
    closesocket(sock);
    //cleanup
    WSACleanup();
}//loose body no send recieve