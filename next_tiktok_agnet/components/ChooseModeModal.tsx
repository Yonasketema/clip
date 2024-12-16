import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const ChooseModeModal = () => {
  const handleOption = (option) => {
    if (option === "tiktok affiliet") {
      window.location.href = "/affiliate";
    } else if (option === "tiktok markating") {
      window.location.href = "/markate";
    }
  };

  return (
    // <Modal>
    //   <h2>Choose an Option</h2>
    //   <button onClick={() => handleOption('tiktok affiliet')}>tiktok affiliet</button>
    //   <button onClick={() => handleOption('tiktok markating')}>tiktok markating</button>
    // </Modal>

    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">Edit Profile</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Edit profile</DialogTitle>
          <DialogDescription>
            Make changes to your profile here. Click save when youre done.
          </DialogDescription>
        </DialogHeader>
        <Button onClick={() => handleOption("tiktok affiliet")}>
          tiktok affiliet
        </Button>
        <Button onClick={() => handleOption("tiktok markating")}>
          tiktok markating
        </Button>
      </DialogContent>
    </Dialog>
  );
};

export default ChooseModeModal;
