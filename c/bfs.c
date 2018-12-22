#include <stdio.h>
#include <stdlib.h>

#define MAXV 1000
#define TRUE 1
#define FALSE 0

typedef struct {
	int y;
	struct edgenode *next;
} edgenode;

typedef struct {
	edgenode *edges[MAXV + 1];
	int degree[MAXV + 1];
	int nvertices;
	int nedges;
	int directed;
} graph;

int init_graph(graph *g, int directed);
void insert_edge(graph *g, int x, int y, int directed);
void set_nvertices(graph *g, int n);
void print_graph(graph *g);

int main() {
	graph *g;
	g = malloc(sizeof(graph));
	init_graph(g, FALSE);
	set_nvertices(g, 4);
	int i;
	for (i = 0; i < 4; i++) {
		insert_edge(g, i % 4, (i + 1) % 4, FALSE);
	}
	print_graph(g);
}

int init_graph(graph *g, int directed) {
	g->nvertices = 0;
	g->nedges = 0;
	g->directed = directed;
	
	int i;
	for (i = 0; i < MAXV; i++) {
		g->edges[i] = NULL;
		g->degree[i] = 0;
	}
}

void insert_edge(graph *g, int x, int y, int directed) {
	edgenode *p;
	p = malloc(sizeof(edgenode));

	p->y = y;
	
	if (g->edges[x] == NULL) {
		g->edges[x] = p;
	}
	else {
		p->next = g->edges[x];
		g->edges[x] = p;
	}
	
	g->degree[x]++;

	if (directed == FALSE)
		insert_edge(g, y, x, TRUE);
	else
		g->nedges++;
}

void set_nvertices(graph *g, int n) {
	g->nvertices = n;
}

/*
typedef struct {
	edgenode *edges[MAXV + 1];
	int degree[MAXV + 1];
	int nvertices;
	int nedges;
	int directed;
} graph;
*/

void print_graph(graph *g) {
	int i;
	for (i = 0; i < g->nvertices; i++) {
		printf("%d: ", i);
		edgenode *current_edge = g->edges[i];
		while (current_edge != NULL) {
			printf("%d ", current_edge -> y);
			current_edge = current_edge->next;
		}
		printf("\n");
	}	
}
