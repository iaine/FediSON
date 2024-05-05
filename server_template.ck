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

.15 => s.gain;

while (true) {
    e => now;
    while (e.nextMsg() != 0) {
        e.getString() => string op;
        <<< "name ", name >>>;
        <<< "op ", op >>>;
        if (op != name) {
             <<< checkBlock(op) >>>;

            if (checkBlock(op) != Std.atoi("-1")) {
                245.32 => s.freq;
            } else {
                60.00 => s.freq;
            }
            1::second => now;
            osnd.startMsg("/fedi, s");
            osnd.addString(name);
        }
    }
}

// find the name. If -1 fail, else
fun int checkBlock(string name) {
    return blocks.find(name + ",");
}