%global assets_version 0.1.0

Name:       urukos-skel
Version:    %{assets_version}
Release:    1%{?dist}
Summary:    Default user configuration for UrukOS (fish, ghostty, tmux, nvim)
URL:        https://github.com/j0yb0y-m/UrukOS-assets
Source0:    https://github.com/j0yb0y-m/UrukOS-assets/archive/refs/tags/v%{assets_version}.tar.gz
License:    MIT
BuildArch:  noarch

Requires:   fish
Requires:   ghostty
Requires:   tmux
Requires:   neovim
Requires:   bat
Requires:   eza

%description
Installs default dotfiles into /etc/skel (fish with the UrukOS theme,
ghostty config, tmux colors, a minimal neovim init) and makes fish the
default shell for NEW users via /etc/default/useradd. Root and existing
users keep their current shells.

%prep
%setup -q -n UrukOS-assets-%{assets_version}

%build

%install
rm -rf %{buildroot}

# fish
mkdir -p %{buildroot}/etc/skel/.config/fish/conf.d
install -p -m 644 terminal/fish/urukos.theme %{buildroot}/etc/skel/.config/fish/conf.d/urukos_theme.fish
cat > %{buildroot}/etc/skel/.config/fish/config.fish << 'EOF'
if status is-interactive
    alias cat 'bat'
    alias ls 'eza --icons'
    alias ll 'eza -la --icons'
end
EOF

# ghostty
mkdir -p %{buildroot}/etc/skel/.config/ghostty/themes
install -p -m 644 terminal/ghostty/urukos %{buildroot}/etc/skel/.config/ghostty/themes/UrukOS
cat > %{buildroot}/etc/skel/.config/ghostty/config << 'EOF'
theme = UrukOS
font-family = JetBrains Mono
EOF

# tmux
mkdir -p %{buildroot}/etc/skel/.config
cat > %{buildroot}/etc/skel/.tmux.conf << 'EOF'
source-file /usr/share/urukos/tmux/urukos.conf
EOF
mkdir -p %{buildroot}%{_datadir}/urukos/tmux
install -p -m 644 terminal/tmux/urukos.conf %{buildroot}%{_datadir}/urukos/tmux/urukos.conf

# bat / eza
mkdir -p %{buildroot}/etc/skel/.config/bat/themes
install -p -m 644 terminal/bat/themes/urukos.tmTheme %{buildroot}/etc/skel/.config/bat/themes/urukos.tmTheme
mkdir -p %{buildroot}%{_datadir}/urukos/eza
install -p -m 644 terminal/eza/theme.yml %{buildroot}%{_datadir}/urukos/eza/theme.yml

# neovim: minimal init, LazyVim starter files are vendored at M5 (see PACKAGING.md)
mkdir -p %{buildroot}/etc/skel/.config/nvim
cat > %{buildroot}/etc/skel/.config/nvim/init.lua << 'EOF'
-- UrukOS neovim defaults. The LazyVim starter is vendored into
-- /etc/skel/.config/nvim at Milestone 5; until then, run
--   git clone https://github.com/LazyVim/starter ~/.config/nvim
-- and remove its .git directory.
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.termguicolors = true
EOF

# fastfetch
mkdir -p %{buildroot}%{_datadir}/urukos
install -p -m 644 terminal/fastfetch/config.jsonc %{buildroot}%{_datadir}/urukos/fastfetch.jsonc
install -p -m 644 terminal/fastfetch/fastfetch-logo.txt %{buildroot}%{_datadir}/urukos/fastfetch-logo.txt

# new users get fish by default
install -d %{buildroot}%{_sysconfdir}/default
cat > %{buildroot}%{_sysconfdir}/default/useradd << 'EOF'
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/usr/bin/fish
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes
EOF

%files
%license LICENSE
%{_datadir}/urukos
%{_sysconfdir}/default/useradd
%dir /etc/skel/.config/fish
%dir /etc/skel/.config/fish/conf.d
/etc/skel/.config/fish/config.fish
/etc/skel/.config/fish/conf.d/urukos_theme.fish
%dir /etc/skel/.config/ghostty
%dir /etc/skel/.config/ghostty/themes
/etc/skel/.config/ghostty/config
/etc/skel/.config/ghostty/themes/UrukOS
/etc/skel/.tmux.conf
%dir /etc/skel/.config/bat
%dir /etc/skel/.config/bat/themes
/etc/skel/.config/bat/themes/urukos.tmTheme
%dir /etc/skel/.config/nvim
/etc/skel/.config/nvim/init.lua

%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 0.1.0-1
- Initial package
