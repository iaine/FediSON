OscRecv orec;
OscSend osnd;

SinOsc s => dac;


// need to set up it on the command line    
$port => orec.port;
osnd.setHost("localhost", $port);

orec.listen();
orec.event("/fedi, s") @=> OscEvent e;

"$name" => string name;
"$blocks" @=> string blocks;



while (true) {
    e => now;
    while (e.nextMsg() != 0) {
        e.getString() => string op;
        if (op != name) {
             <<< checkBlock(op) >>>;

            if (checkBlock(op) != Std.atoi("-1")) {
                <<< "name ", name >>>;
                <<< "op ", op >>>;
                245.32 => s.freq;
                .2 => s.gain;
            } else {
                120.00 => s.freq;
                .25 => s.gain;
            }
            0.2::second => now;
            0.0 => s.freq;
            0.2::second => now;
            osnd.startMsg("/fedi, s");
            osnd.addString(name);
        }
    }
}

// find the name. If -1 fail, else
fun int checkBlock(string name) {
    return blocks.find(name + ",");
}