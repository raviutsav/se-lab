// Primality Test - Time complexity O(sqrt(n))

int isPrime(int n)
{
	if(n == 1) return 0;
	else
	{
		for(int i = 2; i*i <= n; i++)
		{
			if(n%i == 0) return 0;
		}
	}
	return 1;
}



// Sieve Of Eratosthenes  - Time Complexity - O(n log(log n)))
// take n = number upto which you want primes



bool arr[n+1];
for(int i = 0; i <= n; i++) arr[i] = true;

arr[0] = false;
arr[1] = false;

vector<int> primeVec;
for(int i = 2; i*i <= n; i++)
{
	if(arr[i] == 1)
	{
		primeVec.push_back(i);
		for(int j = i*i; j <= n; j = j+i)
		{
			arr[j] = 0;
		}
	}
}



// Prime Factorization efficient program     Time Complexity - O(sqrt(n))


vector<int> primeFactor;

void primeF(int n)
{
	
	while(n%2 == 0)
	{
		primeFactor.push_back(2);
		n = n/2;
	}

	for(int i = 3; i*i <= n; i += 2)
	{
		if(n%i == 0)
		{
			while(n%i == 0)
			{
				primeFactor.push_back(i);
				n = n/i;
			}
		}
	}

	if(n > 1) primeFactor.push_back(n);
}



// Binary Exponentation recursive approach  Time Complexity - O(log n)


int binExp(int base, int exp)
{
	if(exp == 0) return 1;
	int d1 = binExp(base, exp/2);

	else if(exp%2 == 0) return d1*d1;
	else return base*d1*d1;
}



// Binary Exponentiation iterative approach   Time Complexity  -  O(log n)

int binpow(int a, int b) {
    int res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}




// FAST MODULAR EXPONENTIATION

int fastExp(int b, int e, int m)
{
	int result = e & 1 ? b : 1;
	while (e) {
		e >>= 1;
		b = (b * b) % m;
		if (e & 1)
			result = (result * b) % m;
	}
	return result;
}



// Prime Number Test

bool isPrime(int x) {
    for (int d = 2; d * d <= x; d++) {
        if (x % d == 0)
            return false;
    }
    return true;
}



----------------------------------------------------------------------------
								  INVERSE MODULO
----------------------------------------------------------------------------

int inv[m+1];
inv[1] = 1;
for(int i = 2; i < m; ++i)
    inv[i] = m - (m/i) * inv[m%i] % m;






// DFS General code

vector<int> adj[N+1];   // adjacency list
int vis[N+1];

void dfs(int vertex)
{
	if(vis[vertex]) return;
	vis[vertex] = 1;
	//
	for(int i = 0; i < adj[vertex].size(); i++)
	{
		//
		dfs(adj[vertex][i]);
		//
	}
	//
}
