import Buffer "mo:base/Buffer";

actor{

  let name: Text = "dao_adventure";
  var manifesto: Text = "Make web 3.0 democratic!";
  var goals = Buffer.Buffer<Text>(5);

  public shared query func getName() : async Text {
    return name; 
  };

  public shared query func getManifesto() : async Text {
    return manifesto;
  };

  public shared func setManifesto(newManifesto : Text) : async () {
    manifesto := newManifesto;
  };

  public shared func addGoal(newGoal : Text) : async () {
    goals.add(newGoal);
  };

  public shared query func getGoals() : async [Text] {
    return Buffer.toArray(goals);
  };
}