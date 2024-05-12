#include <bits/stdc++.h>
using namespace std;

set <long> AccNumsList;
double min_balance = 5000;


long random9 () {
    int i=0;
    long x=0,a;
    while (i<8){
        a=rand()%(10);
        x=10*x +a;
        i++;
    }
    a=1+(rand()%9);
    x=10*x + a;
 
   if ( AccNumsList.count(x)==1){
    random9();
    return 0;
   }
   else {
    AccNumsList.insert(x);
    return x;
   }
}



class user{
    private :
    string name ;
    string username;
    string password;
    


    public :
    vector <accounts> allaccounts; 
    
    void setname(string x){
       name = x;
    }
    void setusernameforuser (string x){
        username=x;
    }
    void setpasswordforuser (string x){
        password = x;
    }
    void changepasswd() {
        cout << "Enter New Password"<< endl;
        cin >> password;
    }
    void createAccount();
    void getAccount();
    
};



void user :: createAccount(){

accounts SampleAcc;
allaccounts.push_back(SampleAcc) ;

long r = random9();
SampleAcc.account_number=r;
SampleAcc.account_balance=0;

cout << "For Savings Account, ENTER 0"<< endl;
cout << "For Current/Checking Account, ENTER 1"<< endl;
int a;
cin>>a;
if (a==0){

    

}

}



class accounts{
    private :
    long account_number;
    double account_balance;
    vector <string> transaction;


    public :
    friend class user; 
    void deposit  (double money);
    void withdraw (double money);
    void transfer (double money);


};

void accounts::deposit(double money){
    account_balance=account_balance+money;

    string line;
    line = to_string(money) + " (Deposit)";
    transaction.push_back(line);

}

void accounts::withdraw(double money){
    if( account_balance - money < min_balance){
        cout<<"Insufficient Funds"<< endl;
        return;
    }
    account_balance=account_balance-money;

    string line;
    line = to_string(money) +  " has been withdrawn from " ;
    transaction.push_back(line);

}

void accounts::transfer(double money){
    account_balance=account_balance-money;

    string line;
    line = to_string(money) + " (Trasfer)";
    transaction.push_back(line);

}

class savingsacc : public accounts {
    public :

};


int main(){

vector <string> usernameslist;


    while (1){
    cout<< "For Account Holder : ENTER 0"<<endl;
    cout<< "For Branch Manager: ENTER 1"<<endl;
    int a,b;
    cin>> a;
    if (a==0) {
        cout << "For Sign Up, ENTER 0" << endl;
        cout << "For Log In, ENTER 1" << endl;
        cin >> b;
           if (b==0) {
                user sample;
                string str;
                cout << "Enter Full Name"<< endl;
                cin>>str;
                sample.setname(str);

                cout << "Enter Username" << endl;
                cin >> str;
                sample.setusernameforuser(str);

                cout << "Enter Password" << endl;
                cin >> str;
                sample.setpasswordforuser(str);

                // STILL FIGURING OUT TO MODIFY CODE PROPERLY


                


           }

    }
    }

    return 0;
}

