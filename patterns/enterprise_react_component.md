# Pattern: Enterprise React Component (2026 Standard)

> Reference implementation for `skills/web-development`

## File Structure

```text
src/components/UserCard/
├── index.ts          # Public export
├── UserCard.tsx      # Logic & View
├── UserCard.test.tsx # Unit Tests
└── UserCard.stories.tsx # Storybook
```

## Component Template (`UserCard.tsx`)

```tsx
import { useState } from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { User } from '@/types';

// 1. Styling with CVA (Tailwind)
const cardVariants = cva(
  "rounded-lg p-4 border transition-all",
  {
    variants: {
      intent: {
        primary: "bg-white border-gray-200 shadow-sm hover:shadow-md",
        danger: "bg-red-50 border-red-200",
      },
      size: {
        sm: "text-sm",
        md: "text-base",
      }
    },
    defaultVariants: {
      intent: "primary",
      size: "md",
    }
  }
);

// 2. Strong Typing
interface UserCardProps extends VariantProps<typeof cardVariants> {
  user: User;
  onEdit?: (id: string) => void;
  className?: string; // Allow override
}

// 3. Component Definition
export function UserCard({ user, intent, size, className, onEdit }: UserCardProps) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div 
      className={cn(cardVariants({ intent, size }), className)}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      role="article"
      aria-label={`Profile of ${user.name}`}
    >
      <div className="flex items-center gap-3">
        <img 
          src={user.avatar} 
          alt="" 
          className="w-10 h-10 rounded-full bg-gray-100" 
        />
        <div>
          <h3 className="font-semibold">{user.name}</h3>
          <p className="text-gray-500">{user.email}</p>
        </div>
      </div>

      {/* 4. Conditional Rendering */}
      {onEdit && isHovered && (
        <button 
          onClick={() => onEdit(user.id)}
          className="mt-3 w-full py-1 text-xs bg-gray-100 hover:bg-gray-200 rounded"
        >
          Edit Profile
        </button>
      )}
    </div>
  );
}
```
