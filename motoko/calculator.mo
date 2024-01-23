import Float "mo:base/Float";

actor {
    var counter : Float = 0;

    public shared func add(x : Float) : async Float {
        counter += x;
        return counter
    };

    public shared func sub(x : Float) : async Float {
        counter -= x;
        return counter
    };

    public shared func mul(x : Float) : async Float {
        counter *= x;
        return counter;
    };

    public shared func div(x : Float) : async Float {
        counter /= 0;
        return counter
    };

    public shared func reset() : async () {
        counter := 0;
    };

    public shared func see() : async Float {
        return counter;
    };

    public shared func sqrt() : async Float {
        counter := Float.sqrt(counter);
        return counter;
    };

    public shared func floor() : async Int {
        return (Float.toInt(counter));
    };
}