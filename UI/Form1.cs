using System.Windows.Forms;
using System.Drawing;

namespace UI
{
    public partial class Form1 : Form
    {
        private TextBox searchTextBox;
        private Button myButton;
        private PictureBox bannerPictureBox;

        public Form1()
        {
            InitializeComponent();
            AddBanner();
            AddSearchTextBox();
            AddButton();
            CenterComponents();
            ChangeBackgroundColor();
        }
        private void AddBanner()
        {
            bannerPictureBox = new PictureBox();
            bannerPictureBox.Image = Image.FromFile("logo.jpg");
            bannerPictureBox.SizeMode = PictureBoxSizeMode.AutoSize;
            Controls.Add(bannerPictureBox);
        }
        private void AddSearchTextBox()
        {
            searchTextBox = new TextBox();
            searchTextBox.BorderStyle = BorderStyle.FixedSingle;
            searchTextBox.Font = new Font("Tahoma", 14);
            searchTextBox.Size = new Size(400, 30);
            searchTextBox.Text = "search with keyword";
            searchTextBox.ForeColor = Color.Gray;
            searchTextBox.GotFocus += SearchTextBox_GotFocus;
            searchTextBox.LostFocus += SearchTextBox_LostFocus;
            Controls.Add(searchTextBox);
        }

        private void SearchTextBox_GotFocus(object sender, System.EventArgs e)
        {
            if (searchTextBox.Text == "search with keyword")
            {
                searchTextBox.Text = "";
                searchTextBox.ForeColor = Color.Black;
            }
        }

        private void SearchTextBox_LostFocus(object sender, System.EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(searchTextBox.Text))
            {
                searchTextBox.Text = "search with keyword";
                searchTextBox.ForeColor = Color.Gray;
            }
        }

        private void AddButton()
        {
            myButton = new Button();
            myButton.Text = "Search 🔍";
            myButton.BackColor = Color.White;
            myButton.Location = new Point(260, 50);
            myButton.Size = new Size(100, 30);
            myButton.Click += MyButton_Click;
            Controls.Add(myButton);
        }
        private void CenterComponents()
        {
           this.Load += (sender, e) =>
            {
                int centerX = ClientSize.Width / 2;
                int centerY = ClientSize.Height / 2;

                bannerPictureBox.Location = new Point(centerX - bannerPictureBox.Width / 2, centerY - bannerPictureBox.Height - 50);
                searchTextBox.Location = new Point(centerX - searchTextBox.Width / 2, centerY);
                myButton.Location = new Point(centerX + searchTextBox.Width / 2 + 5, centerY);
            };
        }
        private void MyButton_Click(object sender, System.EventArgs e)
        {
            MessageBox.Show("Button clicked!");
        }
        private void ChangeBackgroundColor()
        {
            Color backgroundColor = ColorFromHSL(0, 0, 0.9608);
            this.BackColor = backgroundColor;
        }

        private Color ColorFromHSL(double hue, double saturation, double luminosity)
        {
            double r, g, b;

            if (saturation == 0)
            {
                r = g = b = luminosity;
            }
            else
            {
                double temp2 = luminosity < 0.5 ? luminosity * (1.0 + saturation) : luminosity + saturation - luminosity * saturation;
                double temp1 = 2.0 * luminosity - temp2;

                r = GetColorComponent(temp1, temp2, hue + 1.0 / 3.0);
                g = GetColorComponent(temp1, temp2, hue);
                b = GetColorComponent(temp1, temp2, hue - 1.0 / 3.0);
            }

            return Color.FromArgb((int)(255 * r), (int)(255 * g), (int)(255 * b));
        }

        private double GetColorComponent(double temp1, double temp2, double temp3)
        {
            temp3 = MoveIntoRange(temp3);
            if (temp3 < 1.0 / 6.0)
                return temp1 + (temp2 - temp1) * 6.0 * temp3;
            else if (temp3 < 0.5)
                return temp2;
            else if (temp3 < 2.0 / 3.0)
                return temp1 + (temp2 - temp1) * (2.0 / 3.0 - temp3) * 6.0;
            else
                return temp1;
        }

        private double MoveIntoRange(double temp3)
        {
            if (temp3 < 0.0)
                temp3 += 1.0;
            else if (temp3 > 1.0)
                temp3 -= 1.0;
            return temp3;
        }
    }
}
