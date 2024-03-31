OscRecv orec;
OscSend osnd;

Impulse i => BiQuad f => dac;


// need to set up it on the command line    
5005 => orec.port;
5005 => osnd.port;
orec.listen();
orec.event("/fedi, s") @=> OscEvent e;

string name => "$name"
string[] blocks @=> $block

.99 => f.prad;
// set equal gain zero’s
1 => f.eqzs;
// initialize float variable
0.0 => float v;


while (true) {
    e => now;
    while (e.nextMsg() != 0) {
        e.getString() => string op;
        <<< "op", op >>>;
        int snd <= checkBlock(op);

        if (snd == 1) {
            Std.fabs(Math.sin(v)) * 4000.0 => f.pfreq;
        } else {
            Std.fabs(Math.sin(v)) * 400.0 => f.pfreq;
        }
        osnd.startMsg("/fedi, s");
        osnd.addString(name);
    }
}

func int checkBlock(string name) {
    int blocked => 0;
    for ( 0 => int i; i < blocks.size(); i++ ) {
        if ( name == blocked[i]) blocked => 0;
    }
    return blocked;
}