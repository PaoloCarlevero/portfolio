import Principal "mo:base/Principal";
import Result "mo:base/Result";
import HashMap "mo:base/HashMap";
import Types "types";
import Buffer "mo:base/Buffer";
import Array "mo:base/Array";

actor {

    type Member = Types.Member;
    type Result<Ok, Err> = Types.Result<Ok, Err>;
    type HashMap<K, V> = Types.HashMap<K, V>;

    let members = HashMap.HashMap<Principal, Member>(0, Principal.equal, Principal.hash);

    public shared ({ caller }) func addMember(member : Member) : async Result<(), Text> {
        switch(members.get(caller)) {
          case(?member) {
            return #err("User already exists");
          };
          case(null) {
            members.put(caller, member);
            return #ok();
          };
        }
    };

    public shared ({ caller }) func updateMember(member : Member) : async Result<(), Text> {
        switch(members.replace(caller, member)) {
          case(?member) {
            return #ok();
          };
          case(null) {
            return #err("User doesn't exist");
          };
        }
    };

    public shared ({ caller }) func removeMember() : async Result<(), Text> {
        switch(members.remove(caller)) {
          case(?member) {
            return #ok();
          };
          case(null) {
            return #err("User doesn't exist");
          };
        }
    };

    public query func getMember(p : Principal) : async Result<Member, Text> {
        switch(members.get(p)) {
          case(?member) {
            return #ok(member);
          };
          case(null) {
            return #err("member");
          };
        }
    };

    public query func getAllMembers() : async [Member] {
        let membersBuffer = Buffer.Buffer<Member>(0);

        for (member in members.vals()) {
          membersBuffer.add( member );
        };

        let membersArray = Buffer.toArray(membersBuffer);
        return membersArray;
    };

    public query func numberOfMembers() : async Nat {
        return members.size();
    };

};